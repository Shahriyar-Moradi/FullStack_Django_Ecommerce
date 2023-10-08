<!-- Example buttons for filtering categories -->
<button class="filter-btn" data-category="electronics">Electronics</button>
<button class="filter-btn" data-category="clothing">Clothing</button>

<!-- Example buttons for filtering brands -->
<button class="filter-btn" data-brand="apple">Apple</button>
<button class="filter-btn" data-brand="samsung">Samsung</button>

<!-- Container to display the filtered products -->
<div id="product-container"></div>

<!-- JavaScript code to handle the AJAX request -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  var filterButtons = document.querySelectorAll('.filter-btn');
  var productContainer = document.getElementById('product-container');

  filterButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var category = this.dataset.category;
      var brand = this.dataset.brand;

      fetch('/filter-products?category=' + category + '&brand=' + brand)
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          var products = data.products;
          productContainer.innerHTML = '';

          products.forEach(function(product) {
            var productHtml = `
              <div class="product">
                <p>Name: ${product.name}</p>
                <p>Price: ${product.price}</p>
              </div>
            `;

            productContainer.insertAdjacentHTML('beforeend', productHtml);
          });
        })
        .catch(function(error) {
          console.log('Error:', error);
        });
    });
  });
});
</script>

//
.then((response) =>response.blob())
            .then(data => {
                const imageUrl = URL.createObjectURL(data);
        const imageElement = document.createElement('img');
    imageElement.src = imageUrl;
    imageContainer.appendChild(imageElement);

  })




//


async function load_pic() {

        const url = '<REPLACE-WITH-URL>'

        const options = {
            method: "GET"
        }

        let response = await fetch(url, options)

        if (response.status === 200) {

            const imageBlob = await response.blob()
            const imageObjectURL = URL.createObjectURL(imageBlob);

            const image = document.createElement('img')
            image.src = imageObjectURL

            const container = document.getElementById("your-container")
            container.append(image)
        }
        else {
            console.log("HTTP-Error: " + response.status)
        }
    }




    //
    //
const $btn = document.getElementById('downloadImage')
const url = 'https://s3-ap-southeast-1.amazonaws.com/tksproduction/bmtimages/pY3BnhPQYpTxasKfx.jpeg'

const fetchImage = async url => {
  const response = await fetch(url)
  const blob = await response.blob()

  return blob
}

const downloadImage = async url => {
  const imageBlob = await fetchImage(url)
  const imageBase64 = URL.createObjectURL(imageBlob)

  console.log({imageBase64})

  const a = document.createElement('a')
  a.style.setProperty('display', 'none')
  document.body.appendChild(a)
  a.download = url.replace(/^.*[\\\/]/, '')
  a.href = imageBase64
  a.click()
  a.remove()
}

$btn.onclick = event => downloadImage(url)