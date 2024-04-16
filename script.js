// Lista para armazenar os dados salvos
let dadosSalvos = [];

// Função para carregar os dados do arquivo JSON
async function carregarDados() {
    try {
        // Carrega os dados do arquivo JSON
        const response = await fetch('dados.json');
        if (!response.ok) {
            throw new Error('Erro ao carregar os dados.');
        }
        const dados = await response.json();

        // Se houver dados salvos no arquivo, atribui-os à variável dadosSalvos
        if (dados && Array.isArray(dados)) {
            dadosSalvos = dados;
        }
    } catch (error) {
        console.error('Erro ao carregar os dados:', error);
    }
}

// Função para salvar os dados no arquivo JSON
async function salvarDados() {
    try {
        let nome = document.getElementById('nome').value;
        let idade = document.getElementById('idade').value;
        let salario = document.getElementById('salario').value;

        // Adiciona os dados à lista de dados salvos
        dadosSalvos.push({ nome: nome, idade: idade, salario: salario });

        // Limpa os campos de entrada após salvar os dados
        document.getElementById('nome').value = '';
        document.getElementById('idade').value = '';
        document.getElementById('salario').value = '';

        // Converte os dados para JSON
        const dadosJSON = JSON.stringify(dadosSalvos);

        // Salva os dados no arquivo JSON usando o método POST
        const response = await fetch('dados.json', {
            method: 'POST', // Usa o método POST
            body: dadosJSON,
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Erro ao salvar os dados.');
        }

        console.log("Dados salvos com sucesso!");
    } catch (error) {
        console.error('Erro ao salvar os dados:', error);
    }
}

// Chama a função para carregar os dados ao carregar a página
carregarDados();
