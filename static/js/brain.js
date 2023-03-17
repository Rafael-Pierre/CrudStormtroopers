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
          if (response.ok) {
            form.reset();
            alert('Cadastro realizado com sucesso!');
          } else {
            alert('Erro ao cadastrar');
          }
        })
        .catch(function(error) {
          alert('Erro ao cadastrar');
        });
})

let formEdit = document.querySelector("#formEdit");

formEdit.addEventListener("submit", function(event){
    event.preventDefault();
    event.stopPropagation();
    // crie um objeto FormData com os dados do formulário
    var formData = new FormData(formEdit);

    // envie a requisição utilizando o fetch
    fetch(formEdit.action, {
      method: 'POST',
      body: new URLSearchParams(formData),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
    .then(function(response) {
      if (response.ok) {
        setTimeout(function() {
          alert('Update realizado com sucesso!');
        }, 100);
      } else {
        alert('Erro ao alterar os campos');
      }
    })
    .catch(function(error) {
      alert('Erro ao alterar os campos');
    });
})
    