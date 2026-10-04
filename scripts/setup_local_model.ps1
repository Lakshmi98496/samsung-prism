# Portable CPU inference. Downloads official binaries and model weights into an ignored folder.
$ErrorActionPreference = 'Stop'
$prismRoot = Split-Path -Parent $PSScriptRoot
$prismModelDir = Join-Path $prismRoot '.local-model'
New-Item -ItemType Directory -Force -Path $prismModelDir | Out-Null
$prismZip = Join-Path $prismModelDir 'runtime.zip'
Invoke-WebRequest -Uri 'https://github.com/ggml-org/llama.cpp/releases/download/b11388/llama-b11388-bin-win-cpu-x64.zip' -OutFile $prismZip
Expand-Archive -LiteralPath $prismZip -DestinationPath (Join-Path $prismModelDir 'runtime') -Force
Invoke-WebRequest -Uri 'https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/9217f5db79a29953eb74d5343926648285ec7e67/qwen2.5-0.5b-instruct-q4_k_m.gguf' -OutFile (Join-Path $prismModelDir 'qwen2.5-0.5b.gguf')
Write-Host 'Download complete. Run scripts/start_local_model.ps1.'
