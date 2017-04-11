cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "file": "plugins/cordova-plugin-device/www/device.js",
        "id": "cordova-plugin-device.device",
        "pluginId": "cordova-plugin-device",
        "clobbers": [
            "device"
        ]
    },
    {
        "file": "plugins/cordova-plugin-device/src/browser/DeviceProxy.js",
        "id": "cordova-plugin-device.DeviceProxy",
        "pluginId": "cordova-plugin-device",
        "runs": true
    },
    {
        "file": "plugins/cordova-plugin-sqlite/www/SQLitePlugin.js",
        "id": "cordova-plugin-sqlite.SQLitePlugin",
        "pluginId": "cordova-plugin-sqlite",
        "clobbers": [
            "window.sqlitePlugin",
            "cordova.plugins.sqlitePlugin"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "cordova-plugin-whitelist": "1.3.2",
    "cordova-plugin-device": "1.1.5",
    "cordova-plugin-sqlite": "1.0.3",
    "cordova-plugin-datepicker": "0.9.2"
}
// BOTTOM OF METADATA
});