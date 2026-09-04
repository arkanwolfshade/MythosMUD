$root = "C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium"
Get-ChildItem -LiteralPath $root -Directory | ForEach-Object {
    $g = Join-Path $_.FullName "graphify-out\graph.json"
    $r = Join-Path $_.FullName "graphify-out\GRAPH_REPORT.md"
    $nodes = 0
    $edges = 0
    if (Test-Path -LiteralPath $g) {
        try {
            $json = Get-Content -LiteralPath $g -Raw | ConvertFrom-Json
            $nodes = @($json.nodes).Count
            $edges = @($json.edges).Count
            if (-not $nodes -and $json.PSObject.Properties.Name -contains "node_count") {
                $nodes = $json.node_count
            }
        } catch {
            $nodes = -1
        }
    }
    "{0}`tHasGraph={1}`tHasReport={2}`tNodes={3}`tEdges={4}" -f $_.Name, (Test-Path -LiteralPath $g), (Test-Path -LiteralPath $r), $nodes, $edges
}
