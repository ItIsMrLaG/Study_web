$.getJSON("myJson", ReadFunc);
var myJson = {}
ReadFunc()

function ReadFunc(data){
    console.log(data)
    myJson = data
    var info = String(data) + data.info + ' ' + data.bd
    $('.jason').html(info);
}

function SelectFunc(value) {
    fetch('?value='+ value + '&id=' + 1).then(function(response) {  //just a concatenation
        console.log(response.status);
        $('.select_info').html(value);      //dynamic output of the code to a specific class value - any html code
        //rar += Number.parseInt(value);
    })
}

function RangeFunc(value) {
     $('.range_info').html(value);      //dynamic output of the code to a specific class value - any html code
}

function RadioFunc(value) {
     $('.radio_info').html(value);      //dynamic output of the code to a specific class value - any html code
}