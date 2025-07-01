// Função para abrir o WhatsApp com mensagem pré-definida
function pedirWhatsapp(itemNome) {
    const numero = "54991853581";
    const mensagem = `Olá Mega Lanches! Gostaria de pedir um ${itemNome}.`;
    const url = `https://wa.me/${numero}?text=${encodeURIComponent(mensagem)}`;
    window.open(url, '_blank');
}

// Botão flutuante do WhatsApp
document.addEventListener('DOMContentLoaded', function() {
    // Pode adicionar mais interações aqui se necessário
});

// Simples chatbot de abertura automática

//setTimeout(function() {
//    const shouldOpenChat = confirm("Olá! Precisa de ajuda para fazer seu pedido? Clique em OK para falar conosco no WhatsApp.");
//    if (shouldOpenChat) {
//        const numero = "54991853581";
//        const mensagem = "Olá Mega Lanches! Preciso de ajuda com meu pedido.";
//        const url = `https://wa.me/${numero}?text=${encodeURIComponent(mensagem)}`;
//        window.open(url, '_blank');
    }
// }, 30000); // Abre após 30 segundos
