// Всплывающие меню
const menuButton = document.getElementById('menuButton');
const closeButton = document.getElementById('closeButton');
const menu = document.getElementById('menu');
const overlay = document.getElementById('overlay');

// Функция открытия меню
menuButton.addEventListener('click', () => {
    menu.classList.remove('translate-x-full'); // Показ меню
    overlay.classList.remove('hidden'); // Показ затемнения
    document.body.classList.add('overflow-hidden'); // Блокировка прокрутки страницы
});

// Функция закрытия меню
const closeMenu = () => {
    menu.classList.add('translate-x-full'); // Скрытие меню
    overlay.classList.add('hidden'); // Скрытие затемнения
    document.body.classList.remove('overflow-hidden'); // Возврат прокрутки страницы
};

closeButton.addEventListener('click', closeMenu);
overlay.addEventListener('click', closeMenu);


// // Появление ответа на вопрос в Секции FAQ
// document.addEventListener('DOMContentLoaded', () => {
//   const faqContainer = document.getElementById('faq-container');
  
//   faqContainer.addEventListener('click', (event) => {
//       const item = event.target.closest('[data-index]');
//       if (item) {
//           const answer = item.nextElementSibling;
//           const button = item.querySelector('button');
//           const icon = button.querySelector('img');

//           if (answer.classList.contains('hidden')) {
//               answer.classList.remove('hidden');
//               icon.src = "./images/svg/minus.svg";  // смена на минус
//               button.classList.add('rotate-180');
//           } else {
//               answer.classList.add('hidden');
//               icon.src = "./images/svg/plus.svg";  // смена на плюс
//               button.classList.remove('rotate-180');
//           }
//       }
//   });
// });


