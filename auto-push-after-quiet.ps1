param(
    [int]$IntervalMinutes = 15,
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
Write-Host "Every $IntervalMinutes minutes, changes will be committed and pushed if present."
Write-Host "Press Ctrl+C to stop."

while ($true) {
    Start-Sleep -Seconds ($IntervalMinutes * 60)

    if (Has-GitChanges) {
        Ensure-Branch
        git add -A

        if (Has-GitChanges) {
            $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            git commit -m "Auto push changes $timestamp"
            git push -u $Remote $Branch
            Write-Host "Pushed changes at $(Get-Date)."
        }
    } else {
        Write-Host "No changes at $(Get-Date)."
    }
}
