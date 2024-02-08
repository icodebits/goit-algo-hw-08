# GoIT Algorithms Homework 8

Основна ідея вирішення постановленаї задачі за допомогою купи полягає в тому, щоб постійно об'єднувати два найдовші кабелі, оскільки це призведе до мінімізації витрат.

Узагальнено алгоритм виглядає наступним чином:

1. Створимо купу, де кожен елемент - це довжина одного кабелю.
2. Виконуємо операцію вилучення двічі з купи, щоб отримати два найбільші кабелі.
3. Об'єднаємо ці два кабелі і додаємо їх довжину до загальних витрат.
4. Додаємо об'єднаний кабель назад до купи.
5. Повторюємо кроки 2-4, доки купа не стане порожньою.

Цей процес гарантує, що на кожному кроці об'єднуються два найдовші кабелі, що призводить до мінімізації загальних витрат.