cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "id": "cordova-plugin-device.device",
        "file": "plugins/cordova-plugin-device/www/device.js",
        "pluginId": "cordova-plugin-device",
        "clobbers": [
            "device"
        ]
    },
    {
        "id": "cordova-plugin-sqlite.SQLitePlugin",
        "file": "plugins/cordova-plugin-sqlite/www/SQLitePlugin.js",
        "pluginId": "cordova-plugin-sqlite",
        "clobbers": [
            "window.sqlitePlugin",
            "cordova.plugins.sqlitePlugin"
        ]
    },
    {
        "id": "cordova-plugin-datepicker.DatePicker",
        "file": "plugins/cordova-plugin-datepicker/www/android/DatePicker.js",
        "pluginId": "cordova-plugin-datepicker",
        "clobbers": [
            "datePicker"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "cordova-plugin-whitelist": "1.3.2",
    "cordova-plugin-device": "1.1.5",
    "cordova-plugin-sqlite": "1.0.3",
    "cordova-plugin-datepicker": "0.9.2",
    "cordova-plugin-compat": "1.1.0"
};
// BOTTOM OF METADATA
});