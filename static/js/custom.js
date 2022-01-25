var show = true;

function showCheckboxes(str) {
    var checkboxes = document.getElementsByClassName("checkBoxes"+ str)[0];
    if (show) {
        checkboxes.style.display = "block";
        show = false;
    } else {
        checkboxes.style.display = "none";
        show = true;
    }
}



function getValues(str) {
    var arr = [];
    var all = [];
    values = document.getElementsByClassName('checkBoxes'+str)[0].children;
    for(i of values) {
        all.push(i.children[0].id);
        if(i.children[0].checked) {
            arr.push(i.children[0].id);
        }
    }
    return arr.length === 0 ? all : arr;
}