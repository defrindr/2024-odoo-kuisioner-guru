odoo.define('sistem_penilaian_baru', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var core = require('web.core');

    var ConsoleLogWidget = Widget.extend({
        template: 'ConsoleLogWidgetTemplate',

        start: function () {
            this._logMessage('Widget initialized.');
            return this._super();
        },

        _logMessage: function (message) {
            console.log(message);
        },
    });

    core.action_registry.add('console_log_widget', ConsoleLogWidget);

    return ConsoleLogWidget;
});