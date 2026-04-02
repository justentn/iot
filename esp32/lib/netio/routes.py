from lib.gpio.esp32_board import Esp32Board


def register_routes(server, board: Esp32Board):
    @server.route('/api/moisture')
    def get_moisture():
        raw = board.get_pin_value(36)
        voltage = (raw / 4095) * 3.3
        moisture = (1 - (raw - 1500) / (4095 - 1500)) * 100
        moisture = max(0, min(100, moisture))
        return {
            'raw': raw,
            'voltage': round(voltage, 2),
            'moisture': round(moisture, 1)
        }

    @server.route('/api/toggle', method='POST')
    def toggle(request: dict):
        pin = request.get('pin')

        if pin is None:
            return {'error': 'pin is required'}

        state = board.toggle_pin(pin)
        return {'status': 'ok', 'state': state}
