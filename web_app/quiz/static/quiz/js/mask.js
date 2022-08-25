//Mask para o número de telefone ter um padrão
$(document).ready(function(){
    $('#id_whatsapp_colaborador').mask("(00) 00000-0000", {placeholder: "Número do representante"});
});

//Bloco para colocar placeholder no input
document.getElementById('id_nome_empresa').placeholder = 'Nome da Empresa'
document.getElementById('id_nome_colaborador').placeholder = 'Nome do representante'
document.getElementById('id_funcao_colaborador').placeholder = 'Função do representante'
document.getElementById('id_email_colaborador').placeholder = 'E-mail corporativo'
document.getElementById('id_whatsapp_colaborador').placeholder = 'Número do representante'
document.getElementById('id_senha').placeholder = 'Senha'
