.then(response => response.json())
  .then(data => {
    const imageURL = data.photo_main;
    console.log('imgURl',imageURL)
    const productName = data.brands_products.name;
    console.log('name',productName)

    fetch(imageURL)
      .then(response => {
        response.blob().then(blob => {
          const imgURL = URL.createObjectURL(blob);

          const imgTag = document.createElement('img');
          imgTag.src = imgURL;

          document.body.appendChild(imgTag);
        });

        console.log('Product Name:', productName);
      })
      .catch(error => console.error(error));
  }).catch(error => console.error(error))

