param(
    [int]$QuietMinutes = 15,
    [int]$PollSeconds = 60,
    [string]$Remote = "origin",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -LiteralPath $repoRoot

function Has-GitChanges {
    $status = git status --porcelain
    return -not [string]::IsNullOrWhiteSpace($status)
}

function Ensure-Branch {
    $currentBranch = (git branch --show-current).Trim()
    if ([string]::IsNullOrWhiteSpace($currentBranch)) {
        git checkout -B $Branch | Out-Null
        return
    }

    if ($currentBranch -ne $Branch) {
        git branch -M $Branch | Out-Null
    }
}

Write-Host "Watching $repoRoot for Git changes."
Write-Host "Changes will be committed and pushed after $QuietMinutes quiet minutes."
Write-Host "Press Ctrl+C to stop."

$lastChangeAt = $null
$lastSignature = $null

while ($true) {
    $status = git status --porcelain

    if ([string]::IsNullOrWhiteSpace($status)) {
        $lastChangeAt = $null
        $lastSignature = $null
        Start-Sleep -Seconds $PollSeconds
        continue
    }

    $signature = ($status | Out-String)
    if ($signature -ne $lastSignature) {
        $lastSignature = $signature
        $lastChangeAt = Get-Date
        Write-Host "Detected changes at $lastChangeAt. Waiting for quiet period..."
    }

    $quietFor = (Get-Date) - $lastChangeAt
    if ($quietFor.TotalMinutes -ge $QuietMinutes) {
        Ensure-Branch
        git add -A

        if (Has-GitChanges) {
            $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            git commit -m "Auto push changes $timestamp"
            git push -u $Remote $Branch
            Write-Host "Pushed changes at $(Get-Date)."
        }

        $lastChangeAt = $null
        $lastSignature = $null
    }

    Start-Sleep -Seconds $PollSeconds
}
