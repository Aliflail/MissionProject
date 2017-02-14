$(function(){
    var myTextarea = $('.codemir')[0];

    var editor = CodeMirror.fromTextArea(myTextarea, {
        lineNumbers: true,
        mode:{
            name:"python",

        }
    });

});

