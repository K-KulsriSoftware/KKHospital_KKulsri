var listCount = {};
var fieldInfo = {};
var type_map = {'int': 'number', 'double': 'number', 'string': 'text', 'date': 'date', 'dict': 'dict', 'list': 'list'};

function extractFields($input, parent, fields, level, isInList) {
    for(i in fields) {
        if (fields[i].field_type === 'dict') {
            var $panel = $(`
                <div class="panel panel-default">
                    <div class="panel-heading">` + fields[i].field_name + `</div>
                    <div class="panel-body">
                    </div>
                </div>
            `);
            if (isInList) {
                $panel.append('<button class="btn btn-danger delete_list_item--dict" type="button" generate="">-</button>');
            }
            $input.find('.panel-body:eq('+level+')').append($panel);
            extractFields($input, parent + '[' + fields[i].field_name + ']', fields[i].dict, level+1);
        } else if (fields[i].field_type === 'list') {
            listCount[parent + '[' + fields[i].field_name + ']'] = 0;
            $input.find('.panel-body:eq('+level+')').append(`
                <div class="panel panel-default">
                    <div class="panel-heading">` + fields[i].field_name + `</div>
                    <div class="panel-body">
                        <br>
                        <button class="btn btn-default add_list_item" type="button" field_name="` + parent + '[' + fields[i].field_name + ']' + `" item_type="` + type_map[fields[i].value] + `">+</button>
                    </div>
                </div>
            `);
            fieldInfo[parent + '[' + fields[i].field_name + ']'] = fields[i];
        } else {
            $input.find('.panel-body:eq('+level+')').append(`
                <div class="form-group">
                    <label for="` + fields[i].field_name + `">` + fields[i].field_name + `</label>
                </div>
            `);
            if (typeof(fields[i].note) === typeof([])) {
                var $select = $(`<select class="form-control" name="` + parent + '[' + fields[i].field_name + `]"></select>`);
                var note = fields[i].note;
                for (var j = 0; j < note.length; j++) {
                    $select.append(`<option value="` + note[j] + `">` + note[j] + `</option>`);
                }
                $input.find('.panel-body:eq('+level+')').append($select);
            } else {
                $input.find('.panel-body:eq('+level+')').append(`<input type="` + type_map[fields[i].field_type] + `" class="form-control" id="` + parent + '[' + fields[i].field_name + `]" name="` + parent + '[' + fields[i].field_name + `]">`);
            }
        }
    }
}

if (fields) {
    var $form = $('form');
    for (i in fields) {
        var $input = null;
        if (fields[i].field_type === 'dict') {
            $input = $(`
                <div class="panel panel-default">
                    <div class="panel-heading">` + fields[i].field_name + `</div>
                    <div class="panel-body">
                    </div>
                </div>
            `);
            extractFields($input, fields[i].field_name, fields[i].dict, 0);
        } else if (fields[i].field_type === 'list') {
            listCount[fields[i].field_name] = 0;
            $input = $(`
                <div class="panel panel-default">
                    <div class="panel-heading">` + fields[i].field_name + `</div>
                    <div class="panel-body">
                        <br>
                        <button class="btn btn-default add_list_item" type="button" field_name="` + fields[i].field_name + `" item_type="` + type_map[fields[i].value] + `">+</button>
                    </div>
                </div>
            `);
            fieldInfo[fields[i].field_name] = fields[i]
        } else {
            $input = $(`
                <div class="form-group">
                    <label for="` + fields[i].field_name + `">` + fields[i].field_name + `</label>
                </div>
            `);
            if (typeof(fields[i].note) === typeof([])) {
                var $select = $(`<select class="form-control" name="` + fields[i].field_name + `">` + `</select>`);
                var note = fields[i].note;
                for (var j = 0; j < note.length; j++) {
                    $select.append(`<option value="` + note[j] + `">` + note[j] + `</option>`);
                }
                $input.append($select);
            } else {
                $input.append(`<input type="` + type_map[fields[i].field_type] + `" class="form-control" id="` + fields[i].field_name + `" name="` + fields[i].field_name + `">`);
            }
        }
        $form.find('.input-wrapper').append($input);
    }
}

$('.add_list_item').click(function() {
    var field_name = $(this).attr('field_name');
    var field_type = $(this).attr('item_type');
    var $panelBody = $(this).parent();
    var $item = null;
    if (field_type === 'dict') {
        $item = $(`
            <div class="panel panel-default">
                <div class="panel-heading">` + field_name + `</div>
                <div class="panel-body">
                </div>
            </div>
        `);
        extractFields($item, field_name + '[' + listCount[field_name] + ']', fieldInfo[field_name].dict, 0, true);
        $item.find('.panel-body').append('<br><button class="btn btn-danger delete_list_item--dict" type="button" generate="">-</button>');
    } else {
        $item = $(`
            <div class="list_item" field_name="` + field_name + `">
                <input type="` + field_type + `" class="form-control" id="` + field_name + '[' + listCount[field_name] + `]" name="` + field_name + '[' + listCount[field_name] + `]">
                <button class="btn btn-danger delete_list_item" type="button" generate="">-</button>
            </div>
        `);
    }
    listCount[field_name]++;
    if($panelBody.children('.list_item').length > 0) {
        $item.insertAfter($panelBody.find('.list_item:last'));
    } else if ($panelBody.children('.panel').length > 0) {
        $item.insertAfter($panelBody.children('.panel:last'));
    } else {
        $panelBody.prepend($item);
    }
    bindDeleteItemButton();
});

function bindDeleteItemButton() {
    $('.delete_list_item').unbind();
    $('.delete_list_item--dict').unbind();
    $('.delete_list_item').click(function() {
        var field_name = $(this).parent().attr('field_name');
        var $panelBody = $(this).parent().parent();
        $(this).parent().remove();
        listCount[field_name] = 0
        $panelBody.find('.list_item').each(function(index) {
            $(this).find('input').attr('id', field_name + '[' + index + ']').attr('name', field_name + '[' + index + ']');
            listCount[field_name]++;
        });
    });
    $('.delete_list_item--dict').click(function() {
        $(this).parent().parent().remove();
    });
}
