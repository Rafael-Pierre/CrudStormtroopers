let form = document.querySelector("#formCadastra");

form.addEventListener("submit", function(event){
    event.preventDefault();

        // crie um objeto FormData com os dados do formulário
        var formData = new FormData(form);
    
        // envie a requisição utilizando o fetch
        fetch(form.action, {
          method: 'POST',
          body: new URLSearchParams(formData),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then(function(response) {
          return response.text();
        })
        .then(function(data) {
          console.log(data);
        })
        .catch(function(error) {
          console.error(error);
        });
})

