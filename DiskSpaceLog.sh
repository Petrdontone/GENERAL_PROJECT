Time=$(date "+%H:%M:%S")
Day=$(env LC_TIME=ru_RU.UTF-8 date "+%A")
echo "$Day"
echo "$Time"
if [ "$Day" = "воскресенье" ]; then
>Disk_Space.log
  echo "Файл очищен"
else
  echo "Очистка файла делается только в воскресенье"
fi
if [[ "$Time" > "09:00" ]] && [[ "$Time" < "21:00" ]]; then
  echo "Лог файл выгружается только в не рабочее время"   
else
Log=Disk_space.log
Date >> $Log && df >> $Log && cat Disk_space.log
  echo "Лог файл сформирован и сохранен"
fi
if [ "$Day" = "воскресенье" ]; then
name=$(date "+%d.%m.%Y")
tar -czf "$name".tar.gz Disk_space.log
  echo "Файл заархивирован и перемещен в архив"
else
  echo "Архивация делается только в воскресенье"
fi