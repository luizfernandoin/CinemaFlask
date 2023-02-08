'use strict';

window.onload = function gallery() {
    loadGallery()
};

const searchImages = async(text)=> {
    const key = '53946516f41af3e0ac2f77293e9eb855';
    const url = `https://api.themoviedb.org/3/movie/popular?api_key=${key}&language=pt-BR`;
    const response = await fetch(url);
    console.log(response.json())
    return response.json();
};

const createCard = ({links}) => {
    const card = document.createElement('div');
    //console.log(links[0].href)
    card.classList.add('card-container');
    card.innerHTML = `
    <img src=${links[0].href} >
    `;
    return card;
};

const loadGallery = async (text = '', page = 1) => {
    const container = document.querySelector('.container-gallery');
    const {collection} = await searchImages(`${text}&page=${page}`);
    console.log(collection);
    const itens = collection.items;
    const paginas = collection.metadata;
    const cards = itens.map(createCard);
    container.replaceChildren(...cards);
    
    const totalPages = Math.ceil(paginas.total_hits / 100);
    this.tp = totalPages;
    console.log(totalPages)
    document.querySelector('#page').innerHTML = `${page}`;
};

const handleKeypress = ({key, target}) => {
    if (key === 'Enter') {
        loadGallery(target.value);
    }
};

const handleNext = () => {
    let page = Number(document.getElementsByClassName('page')[0].textContent);
    const text = document.querySelector('#search-input').value;
    if (page < tp){
        page++;
        loadGallery(text, page)
    }
};

const handlePrevious = () => {
    let page = Number(document.getElementsByClassName('page')[0].textContent);
    const text = document.querySelector('#search-input').value;
    if (page > 1) {
        page--;
        loadGallery(text, page);
    }
};

const handleFirst = () => {
    let page = Number(document.getElementsByClassName('page')[0].textContent);
    const text = document.querySelector('#search-input').value;
    if (page > 1) {
        loadGallery(text, 1);
    }
};

const handleLast = () => {
    let page = Number(document.getElementsByClassName('page')[0].textContent);
    const text = document.querySelector('#search-input').value;
    const totalPages = tp
    console.log(totalPages)
    if (page != totalPages) {
        if (totalPages > 100){
            loadGallery(text, 100);
        }
        else{
            loadGallery(text, totalPages);
        }
    }
};

document.querySelector('#search-input').addEventListener('keypress', handleKeypress);
document.querySelector('#page-next').addEventListener('click', handleNext);
document.querySelector('#page-previous').addEventListener('click', handlePrevious);
document.querySelector('.first').addEventListener('click', handleFirst);
document.querySelector('.last').addEventListener('click', handleLast);