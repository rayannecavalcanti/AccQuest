Feature: Gerenciamento de Livros na API DemoQA
  Como um usuário da API DemoQA
  Eu quero poder criar um usuário, listar livros, alugar livros e ver detalhes
  Para gerenciar minha experiência de leitura

  Scenario: Criar um usuário, alugar e listar livros
    Given Eu crio um usuário com nome "teasdssasdtUser456" e senha "Tedsst@123"
    And Eu gero um token de acesso
    And Eu listo os livros disponíveis
    When Eu escolho os livros com ISBNs "9781449325862" e "9781449331818" para alugar
    Then Os livros devem ser alugados com sucesso
    And Eu devo ver os detalhes do usuário com os livros alugados