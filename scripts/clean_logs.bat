@echo off
REM Remove runtime logs under repo-root logs/ (directory is gitignored; script lives in scripts/).
set "ROOT=%~dp0.."
cd /d "%ROOT%"
if exist logs rd /s /q logs
mkdir logs
