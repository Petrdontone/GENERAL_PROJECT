if [ -e /c/Users/Vadim/general_project/GENERAL_PROJECT/students.txt ]; then
  rm /c/Users/Vadim/general_project/GENERAL_PROJECT/students.txt
  echo "Список студентов очищен"
 else
  echo "Списка студентов нет"
fi
for students in Вадим Андрей Света Лера
do
echo "$students" >> students.txt
done
echo "Преподаватель: Пётр" && echo "Список студентов:" && sort -d  students.txt && echo "К доске идет:" && cat students.txt | shuf -n1
