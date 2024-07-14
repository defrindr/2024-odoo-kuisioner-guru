odoo.define('sistem_penilaian_baru.GroupedWidget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    var core = require('web.core');
    var ajax = require('web.ajax');

    var QWeb = core.qweb;

    var GroupedWidget = AbstractField.extend({
        template: 'GroupedWidgetTemplate',

        init: function () {
            this._super.apply(this, arguments);
            this.grouped_data = {};
        },

        willStart: function () {
            var self = this;
            return this._rpc({
                model: 'mpenilaian.kepsek.detail',
                method: 'get_grouped_data',
                args: [],
            }).then(function (result) {
                self.grouped_data = result;
            });
        },

        _render: function () {
            this.$el.html(QWeb.render('GroupedWidgetTemplate', {
                widget: this,
                grouped_data: this.grouped_data,
            }));
        },
    });

    fieldRegistry.add('grouped_widget', GroupedWidget);

    return GroupedWidget;
});

console.log(1)
