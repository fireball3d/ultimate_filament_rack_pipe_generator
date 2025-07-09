difference() {
	cylinder($fn = 6, h = 120, r = 14.866769431632862);
	translate(v = [0, 0, 0]) {
		union() {
			cylinder(d = 20.3, h = 36);
			linear_extrude(height = 36, twist = 5400) {
				polygon(points = [[9.6, 0], [10.0, 0.5], [9.6, 1], [0, 1], [0, 0]]);
			}
		}
	}
	translate(v = [0, 0, 85]) {
		union() {
			cylinder(d = 20.3, h = 36);
			linear_extrude(height = 36, twist = 5400) {
				polygon(points = [[9.6, 0], [10.0, 0.5], [9.6, 1], [0, 1], [0, 0]]);
			}
		}
	}
}
