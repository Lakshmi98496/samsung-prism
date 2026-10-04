$ErrorActionPreference = 'Stop'
$prismRoot = Split-Path -Parent $PSScriptRoot
$prismModelDir = Join-Path $prismRoot '.local-model'
$prismServer = Get-ChildItem -LiteralPath (Join-Path $prismModelDir 'runtime') -Filter 'llama-server.exe' -Recurse | Select-Object -First 1
if (-not $prismServer) { throw 'Run scripts/setup_local_model.ps1 first.' }
& $prismServer.FullName -m (Join-Path $prismModelDir 'qwen2.5-0.5b.gguf') --host 127.0.0.1 --port 8081 -c 8192 -t 4 --alias 'qwen2.5-0.5b'
