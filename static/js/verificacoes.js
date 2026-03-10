//let nome = prompt("como você chama?")

//if (nome == null) {
//    alert("recarregue a pagina")
//} else {
//   let correto = confirm("você se chama" + nome + "?")

//  if (correto) {
//       alert(nome + " Bem vindo ao site de cursos")
//  } else {
//       alert("recarregue a pagina")
//   }

//}

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''


}

function limpaInputsCadastro() {
    const inputNome = document.getElementById('input-nome')
    const inputNascimento = document.getElementById('input-nascimento')
    const inputCPF = document.getElementById('input-cpf')
    const inputEmaill = document.getElementById('input-emaill')
    const inputCargo = document.getElementById('input-cargo')
    const inputSalario = document.getElementById('input-salario')

    inputNome.value = ''
    inputNascimento.value = ''
    inputCPF.value = ''
    inputEmaill.value = ''
    inputCargo.value = ''
    inputSalario.value = ''
}


document.addEventListener("DOMContentLoaded", function () {
    const formlogin = document.getElementById('form-login')

    formlogin.addEventListener("submit", function (event) {
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        //senha
        if (inputSenha.value == '') {
            inputSenha.classList.add('is-invalid')
            temErro = True

        } else {
            inputEmail.classList.remove('is-invalid')
        }

        //verificar se os inputs estão vazios - EMAIL
        if (inputEmail.value == '') {
            inputEmail.classList.add('is-invalid')
            temErro = True

        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (temErro) {
            // evita de enviar o formulario
            event.preventDefault()
            alert("preencha todos os campos")
        }

    })


    const formCadastro = document.getElementById('form-cadastro')

    formCadastro.addEventListener("submit", function (event) {
        const inputNome = document.getElementById('input-nome')
        const inputNascimento = document.getElementById('input-nascimento')
        const inputCPF = document.getElementById('input-cpf')
        const inputEmaill = document.getElementById('input-emaill')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        //senha
        if (inputNome.value == '') {
            inputNome.classList.add('is-invalid')
            temErro = True

        } else {
            inputNome.classList.remove('is-invalid')
        }


        if (inputNascimento.value == '') {
            inputNascimento.classList.add('is-invalid')
            temErro = True

        } else {
            inputNascimento.classList.remove('is-invalid')
        }


        if (inputCPF.value == '') {
            inputCPF.classList.add('is-invalid')
            temErro = True

        } else {
            inputCPF.classList.remove('is-invalid')
        }

        if (inputEmaill.value == '') {
            inputEmaill.classList.add('is-invalid')
            temErro = True

        } else {
            inputEmaill.classList.remove('is-invalid')
        }


        if (inputCargo.value == '') {
            inputCargo.classList.add('is-invalid')
            temErro = True

        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value == '') {
            inputSalario.classList.add('is-invalid')
            temErro = True

        } else {
            inputSalario.classList.remove('is-invalid')
        }

        if (temErro) {
            // evita de enviar o formulario
            event.preventDefault()
            alert("preencha todos os campos")
        }

    })
})
