function decheckRest(checkbox){
    const checkboxDiv = document.querySelectorAll('.check-item-container');
    checkboxDiv.forEach(div => {
        const box = div.querySelector('input');
        if (box !== checkbox){
            box.checked = false;
        }
    });
}