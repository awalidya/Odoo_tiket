odoo.define('helpdesk_ticket.iframe_dashboard', function (require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var Qweb = core.qweb;
    var iframe_dashboard = AbstractAction.extend({
        template: 'iFrameDashboard',
        events: {
        },
        function: function(parent, action) {
            this._super(parent, action);
        },
        start: function() {
            var self = this;
            this.set("tittle", 'Dashboard');
            //self.load_data();
        },
        load_data: function () {
            //self.$('.table_view').html(Qweb.render('iFrameDashboard'));
            },
    });
    core.action_registry.add("iframe_dashboard_client", iframe_dashboard);
    return iframe_dashboard;
});