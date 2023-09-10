// <!-- Add to cart buttons -->
//
// <!-- JavaScript code -->
//
//     document.addEventListener("DOMContentLoaded", function() {
//         const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
//         const cartCountElement = document.getElementById('cart-count');
//
//         function addToCart(productId) {
//             const xhr = new XMLHttpRequest();
//             xhr.open("POST", `/add-to-cart/${productId}/`, true);
//             xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//
//             xhr.onreadystatechange = function () {
//                 if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
//                     const response = JSON.parse(xhr.responseText);
//                     updateCartDisplay(response.cart_items_count);
//                 }
//             };
//
//             xhr.send();
//         }
//
//         function updateCartDisplay(count) {
//             cartCountElement.textContent = count;
//         }
//
//         addToCartButtons.forEach(function (button) {
//             button.addEventListener('click', function () {
//                 const productId = button.dataset.productId;
//                 addToCart(productId);
//             });
//         });
//     });
