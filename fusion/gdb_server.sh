# start gdbserver for level00
sudo gdbserver :9898 --attach `ps -A | grep level00 | tail -n1 | cut -d' ' -f2`

# gdb connect
target remote fusion:9898

# read symbols
file level00/level00
