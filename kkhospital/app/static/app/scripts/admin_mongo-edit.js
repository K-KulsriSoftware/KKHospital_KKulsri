var listCount = {};
var fieldInfo = {};
var type_map = {'int': 'number', 'double': 'number', 'string': 'text', 'date': 'date', 'dict': 'dict', 'list': 'list'};

function extractFields($input, parent, fields, level, data, isInList) {
    for(var i = 0; i < fields.length; i++) {
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
            extractFields($input, parent + '[' + fields[i].field_name + ']', fields[i].dict, level+1, data && data[fields[i].field_name] ? data[fields[i].field_name] : null);
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
            if (data && data[fields[i].field_name]) {
                var $parent = $input.find('.panel-body:eq('+(level + 1)+')');
                var field_name = parent + '[' + fields[i].field_name + ']';
                var field_type = type_map[fields[i].value];
                for (var j = 0; j < data[fields[i].field_name].length; j++) {
                    if (field_type === 'dict') {
                        $item = $(`
                            <div class="panel panel-default list-item">
                                <div class="panel-heading">` + field_name + `</div>
                                <div class="panel-body">
                                </div>
                            </div>
                        `);
                        extractFields($item, field_name + '[' + listCount[field_name] + ']', fields[i].dict, level, data[fields[i].field_name][j]);
                        $item.find('.panel-body').append('<br><button class="btn btn-danger delete_list_item--dict" type="button" generate="">-</button>');
                    } else {
                        $item = $(`
                            <div class="list_item" field_name="` + field_name + `">
                                <input type="` + field_type + `" class="form-control" id="` + field_name + '[' + listCount[field_name] + `]" name="` + field_name + '[' + listCount[field_name] + `]" value="` + data[fields[i].field_name][j] + `">
                                <button class="btn btn-danger delete_list_item" type="button" generate="">-</button>
                            </div>
                        `);
                    }
                    listCount[field_name]++;
                    if($parent.children('.list_item').length > 0) {
                        $item.insertAfter($parent.find('.list_item:last'));
                    } else if ($parent.children('.panel').length > 0) {
                        $item.insertAfter($parent.children('.panel:last'));
                    } else {
                        $parent.prepend($item);
                    }
                    bindDeleteItemButton();
                }
            }
        } else {
            var $tmp = $(`
                <div class="form-group">
                    <label for="` + fields[i].field_name + `">` + fields[i].field_name + `</label>
                </div>
            `);
            if (fields[i].note && Array.isArray(fields[i].note)) {
                var $options = $(`
                    <select class="form-control" id="` + parent + '[' + fields[i].field_name + `]" name="` + parent + '[' + fields[i].field_name + `]">
                    </select>
                `)
                $.each(fields[i].note, function(index, value) {
                    $options.append(`<option value="` + value + `" ` + (data && data[fields[i].field_name] && data[fields[i].field_name] === value ? 'selected' : '') +`>` + value + `</option`);
                });
                $tmp.append($options);
                $input.find('.panel-body:eq('+level+')').append($tmp);
            } else {
                $tmp.append(`<input type="` + type_map[fields[i].field_type] + `" class="form-control" id="` + parent + '[' + fields[i].field_name + `]" name="` + parent + '[' + fields[i].field_name + `]" value="` + (data && data[fields[i].field_name] ? data[fields[i].field_name] : '') + `">`);
                $input.find('.panel-body:eq('+level+')').append($tmp);
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
            extractFields($input, fields[i].field_name, fields[i].dict, 0, data[fields[i].field_name]);
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
            if (data && data[fields[i].field_name]) {
                var $parent = $input.find('.panel-body');
                var field_name = fields[i].field_name;
                var field_type = type_map[fields[i].value];
                for (var j = 0; j < data[fields[i].field_name].length; j++) {
                    if (field_type === 'dict') {
                        $item = $(`
                            <div class="panel panel-default">
                                <div class="panel-heading">` + field_name + `</div>
                                <div class="panel-body">
                                </div>
                            </div>
                        `);
                        extractFields($item, field_name + '[' + listCount[field_name] + ']', fields[i].dict, level, data[fields[i].field_name][j], true);
                    } else {
                        $item = $(`
                            <div class="list_item" field_name="` + field_name + `">
                                <input type="` + field_type + `" class="form-control" id="` + field_name + '[' + listCount[field_name] + `]" name="` + field_name + '[' + listCount[field_name] + `]" value="` + data[fields[i].field_name][j] + `">
                                <button class="btn btn-danger delete_list_item" type="button" generate="">-</button>
                            </div>
                        `);
                    }
                    listCount[field_name]++;
                    if($parent.children('.list_item').length > 0) {
                        $item.insertAfter($parent.find('.list_item:last'));
                    } else if ($parent.children('.panel').length > 0) {
                        $item.insertAfter($parent.children('.panel:last'));
                    } else {
                        $parent.prepend($item);
                    }
                    bindDeleteItemButton();
                }
            }
        } else {
            var thisFieldData = data[fields[i].field_name];
            if (fields[i].field_type === 'date' && fields[i].note === 'without hour') {
                thisFieldData = thisFieldData.split(' ')[0];
            }
            $input = $(`
                <div class="form-group">
                    <label for="` + fields[i].field_name + `">` + fields[i].field_name + `</label>
                </div>
            `);
            if (fields[i].note && Array.isArray(fields[i].note)) {
                var $options = $(`
                    <select class="form-control" id="` + fields[i].field_name + `" name="` + fields[i].field_name + `">
                    </select>
                `)
                $.each(fields[i].note, function(index, value) {
                    $options.append(`<option value="` + value + `" ` + (thisFieldData === value ? 'selected' : '') +`>` + value + `</option`);
                });
                $input.append($options);
            } else {
                $input.append(`
                    <input type="` + type_map[fields[i].field_type] + `" class="form-control" id="` + fields[i].field_name + `" name="` + fields[i].field_name + `" value="` + thisFieldData + `">
                `);
            }
        }
        $form.find('.input-wrapper').append($input);
    }
}

bindDeleteItemButton();

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

$('form').submit(function() {
    var isConfirmed = confirm('ยืนยันการแก้ไขข้อมูล');
    return isConfirmed;
});
