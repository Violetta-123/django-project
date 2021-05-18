document.addEventListener('DOMContentLoaded', () => {
 
  // Кнопка по которой происходит клик
  let callBackButton = document.getElementById('coll5');
 
  // Модальное окно, которое необходимо открыть
  let modal1 = document.getElementById('modal_reg');
 
  // Кнопка "закрыть" внутри модального окна
  let closeButton = modal1.getElementsByClassName('modal_close')[0];

  let tagBody = document.getElementsByTagName('body');

  callBackButton.onclick = function () {
    modal1.classList.add('modal_active');
    //    (modal_reg).addClass('modal_active');
    tagBody.classList.add('hidden');
  }
 
  closeButton.onclick = function () {
    modal1.classList.remove('modal_active');
    tagBody.classList.remove('hidden');
  }
});

modal_reg.onmousedown = function (e) {
  let target = e.target;
  let modalContent = modal_reg.getElementsByClassName('modal__content')[0];
  if (e.target.closest('.' + modalContent.className) === null) {
    this.classList.remove('modal_active');
    tagBody.classList.remove('hidden');
  }
};
