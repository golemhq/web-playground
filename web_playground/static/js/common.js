
var Common = new function(){

    this.clickable_button = function(id, attrs){
        let attrString = attrs ? attrs.join(' ') : '';
        let button = [
            '<div id="'+id+'-container">',
            '<button id="'+id+'" '+attrString,
                'class="btn btn-primary"',
                'onclick="$(\'#'+id+'-result\').html(\'Clicked!\')">Click Me</button>',
            '<span id="'+id+'"-result" class="button-result"></span>',
            '</div>']; // damn you ie11!!!
        return $(button.join('\n'))
    }

    this.writable_input = function(id, attrs){
        let attrString = attrs ? attrs.join(' ') : '';
        let writable = [
            '<div id="'+id+'-container">',
            '<input type="text" class="form-control" id="'+id+'" '+ attrString,
            'onkeyup="$(\'#'+id+'-input-result\').html(\'Welcome \' + $(this).val());">',
            '<span id="'+id+'"-input-result" class="button-result"></span>',
            '</div>'];
        return $(writable.join('\n'))
    }
}