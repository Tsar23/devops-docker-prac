#!/bin/bash

# Демонстрація робочого процесу Git (Практична 5)
# Студент: Цар Володимир | Група: КН-32сп

echo "1. Створення нової гілки feature-new..."
# git branch feature-new
# git checkout feature-new

echo "2. Внесення змін у файли та їх фіксація..."
# git add .
# git commit -m "feat: додано новий функціонал у гілці feature-new"

echo "3. Повернення до основної гілки (main)..."
# git checkout main

echo "4. Злиття гілки feature-new з основною гілкою..."
# git merge feature-new

echo "5. Симуляція вирішення конфліктів (редагування файлів вручну)..."
# Після ручного редагування:
# git add .
# git commit -m "Merge: вирішено конфлікти між main та feature-new"

echo "Робочий потік успішно завершено."