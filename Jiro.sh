if [ "`stat source/Jiro.py | grep -o x`" == "" ]; then
  chmod +x source/Jiro.py
fi

./source/Jiro.py "$@"
