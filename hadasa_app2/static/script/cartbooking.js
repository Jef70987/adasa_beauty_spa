
const imageStack = [];

function renderCart() {
    const bookingCart = document.getElementById('booking_cart');
    bookingCart.innerHTML = ''; // clear cart
    
    imageStack.forEach((src, index) => {
        const cartItem = document.createElement('li');
        cartItem.style.listStyle = 'none';
        cartItem.style.display = 'flex';
        cartItem.style.margin = '5px';

        const img = document.createElement('img');
        img.src = src;
        img.style.width = '50px';
        img.style.marginRight = '50px';
        img.style.border = '2px solid #ccc';
        img.style.height = '50px';
        
        const btn = document.createElement('button');
        btn.innerText = 'remove';
        btn.style.alignSelf = 'left';
        btn.style.background = 'red';
        btn.style.marginLeft = '50px';
        btn.style.color = 'white';
        btn.style.border = 'none';
        btn.style.fontSize = '10px';
        btn.style.width = '100px';
        btn.style.height = '20px';
        btn.onclick = () => popImage (index); //pass index to remove specific image
        cartItem.appendChild(img);
        cartItem.appendChild(btn);
        bookingCart.appendChild(cartItem);
        
    });
}
function popImage(index){
    //remove an image at a specific index
    imageStack.splice(index, 1);
    renderCart();
}

window.onload = function () {
    const galleryImages = document.querySelectorAll('.gallery-image');

    galleryImages.forEach(img => {
        img.addEventListener('click', () => {
            const wantToBook = confirm("Do You Want To Add To Booking Cart ?");
            if (wantToBook){
                imageStack.push(img.src);
                renderCart();
            }
        });
    });
};
