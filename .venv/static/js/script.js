function validarSenhaCadastro() {
    const senha = document.getElementById("senha").value;
    const confirmarSenha = document.getElementById("confirmar_senha").value;
    if (senha !== confirmarSenha) {
        alert("As senhas não coincidem!");
        return false;
    }
    return true;
}

// Criação do codigo js com confirmação de senha