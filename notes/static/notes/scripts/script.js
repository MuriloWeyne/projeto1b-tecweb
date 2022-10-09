const validateCreateForm = () => {
    let titleInput = document.getElementsByTagName('input')[0].value;
    let descriptionInput = document.getElementsByTagName('textarea')[0].value;
    if (titleInput.length === 0) {
        alert('Preencha o campo do título do post it!');
    } if (descriptionInput.length === 0) {
        alert('Preencha o campo da descrição do post it!');
    }
}

const validateEditForm = () => {
    let titleInput = document.getElementsByClassName('edit-title-input')[0].value;
    let descriptionInput = document.getElementsByClassName('edit-details-input')[0].value;
    if (titleInput.length === 0) {
        alert('Preencha o campo do título!');
    } if (descriptionInput.length === 0) {
        alert('Preencha o campo do conteudo do post it!');
    }
}