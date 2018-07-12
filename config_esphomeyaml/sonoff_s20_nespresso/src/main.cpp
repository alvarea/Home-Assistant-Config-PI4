// Auto generated code by esphomeyaml
#include "esphomelib/application.h"

using namespace esphomelib;

void setup() {
  // ===== DO NOT EDIT ANYTHING BELOW THIS LINE =====
  // ========== AUTO GENERATED CODE BEGIN ===========
  App.set_name("sonoff_s20_nespresso");
  App.init_log();
  auto *wificomponent = App.init_wifi();
  wificomponent->set_sta(WiFiAp{
      .ssid = "TC.alvarea.net",
      .password = "3286202581200",
      .channel = -1,
      .manual_ip = ManualIP{
      .static_ip = IPAddress(192, 168, 0, 33),
      .gateway = IPAddress(192, 168, 0, 1),
      .subnet = IPAddress(255, 255, 255, 0),
      .dns1 = IPAddress(0, 0, 0, 0),
      .dns2 = IPAddress(0, 0, 0, 0),
    },
  });
  auto *otacomponent = App.init_ota();
  otacomponent->start_safe_mode();
  App.init_mqtt("192.168.0.23", 1883, "switch_sonoff", "7xnQj7RUc05dHqywDM");
  auto application_makestatusbinarysensor = App.make_status_binary_sensor("Sonoff S20 Nespresso Status");
  auto application_makegpioswitch = App.make_gpio_switch("Sonoff S20 Nespresso", 12);
  auto application_makegpiobinarysensor = App.make_gpio_binary_sensor("Sonoff S20 Nespresso Bot\303\263n", GPIOInputPin(0, INPUT_PULLUP, true));
  auto *s20_green_led = App.make_esp8266_pwm_output(GPIOOutputPin(13, OUTPUT, true));
  auto application_makelight = App.make_monochromatic_light("Sonoff S20 Nespresso LED", s20_green_led);
  // =========== AUTO GENERATED CODE END ============
  // ========= YOU CAN EDIT AFTER THIS LINE =========
  App.setup();
}

void loop() {
  App.loop();
  delay(16);
}
