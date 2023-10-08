

var updateBtns = document.getElementsByClassName('update-cart')
var user = '{{request.user}}'
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
        var user = '{{ user.username }}';
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user === 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
            console.log("data:",data)
		    location.reload()
		});
}


function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'decrease'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	if (action == 'remove'){
		// cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}





// Create a promise with a listener that returns true
const promiseWithListener = new Promise((resolve, reject) => {
  // Simulate an asynchronous operation
  setTimeout(() => {
    // Check if the message channel is still open
    if (Math.random() < 0.5) {
      // The channel closed before receiving a response
      reject(new Error('A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received.'));
    } else {
      // Resolve the promise with a response
      resolve('Success!');
    }
  }, 1000);
});

// Handle the promise
promiseWithListener
  .then(response => {
    // Handle the successful response
    console.log(response);
  })
  .catch(error => {
    // Handle the error caused by a closed message channel
    if (error.message.includes('A listener indicated an asynchronous response by returning true')) {
      console.error('An error occurred: The message channel closed before a response was received.');
      // Perform any necessary actions or show an appropriate error message to the user
    } else {
      // Handle other types of errors
      console.error(error);
    }
  });



//



//
// const productContainer = document.getElementById('product-container');
// var filterBtns = document.getElementsByClassName('filter-checkbox')
// var user = '{{request.user}}'

// for (i = 0; i < filterBtns.length; i++) {
// 	filterBtns[i].addEventListener('click', function(){
//         let category_id=this.dataset.category
// 		var brandId = this.dataset.brand
// 		var action = this.dataset.action
//         var user = '{{ user.username }}';
// 		console.log('brandId:',brandId, 'Action:', action,'category_id',category_id)
// 		console.log('USER:', user)
//
// 		if (user === 'AnonymousUser'){
// 			addCookieItem(brandId, action)
// 		}else{
//             console.log('authenticated')
// 			updateBrand(brandId, action,)
// 		}
// 	})
// }
// function updateBrand(brandId){
// 	console.log('User is authenticated, sending brand data...')
//     const path = window.location.pathname;
//     const pathParts = path.split('/'); // Split the path by '/'
//     const category_id = parseInt(pathParts[pathParts.length - 2]); // Assuming the category ID is the second-to-last segment in the path
//     console.log(category_id);
//
// 		var url = `/categories/${category_id}/brand/${brandId}/`
//
// 		fetch(url, {
// 			method:'GET',
// 			headers:{
// 				'Content-Type':'application/json',
// 				'X-CSRFToken':csrftoken,
// 			},
//
// 			{#body:JSON.stringify({'brandId':brandId, 'action':action})#}
// 		})
// 		.then((response) => {
// 		   return response.json();
// 		}).then(data => {
//     data.brands_products.forEach(product => {
//       const productHTML = `
//         <div class="product-card">
//           <h3>${product.name}</h3>
//           <p>Price: $${product.price}</p>
//           <img style="max-height: 700px;max-width: 550px" class="card-img-top" src="${product.photo_main.url}" alt="">
//
//         </div>
//       `;
//
//       productContainer.insertAdjacentHTML('beforeend', productHTML);
//     });
//   })
//



// }
// var filterBtns = document.getElementsByClassName('filter-checkbox').addEventListener('click', fetchProducts);
// for (i = 0; i < filterBtns.length; i++) {
// 	filterBtns[i].addEventListener('click', function(){
//         let category_id=this.dataset.category
// 		var brandId = this.dataset.brand
// 		var action = this.dataset.action
//         var user = '{{ user.username }}';
// 		console.log('brandId:',brandId, 'Action:', action,'category_id',category_id)
// 		console.log('USER:', user)
//
// 		if (user === 'AnonymousUser'){
// 			addCookieItem(brandId, action)
// 		}else{
//             console.log('authenticated')
// 			updateBrand(brandId, action,)
// 		}
// 	})
// }
