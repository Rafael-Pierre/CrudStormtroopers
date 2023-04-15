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

$(document).ready(function() {
    var formData = new FormData(this);

    alert("Os dados serão atualizados");
    $.ajax({
      url: "/edit",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
    })
    .done(function(data) {
      // exibe uma mensagem de sucesso
      alert("Update realizado com sucesso!");
      // limpa os campos do formulário
      formEdit.reset();
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      // exibe uma mensagem de erro
      alert("Erro ao alterar os campos: " + errorThrown);
    });;
});

