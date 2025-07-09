difference() {
	cylinder($fn = 6, h = 120, r = 14.866769431632862);
	translate(v = [0, 0, 0]) {
		difference() {
			cylinder(d = 20.4, h = 36);
			linear_extrude(height = 36, twist = 5184.0) {
				polygon(points = [[9.4, 0], [10.6, 1.25], [9.4, 2.5]]);
			}
		}
	}
	translate(v = [0, 0, 85]) {
		difference() {
			cylinder(d = 20.4, h = 36);
			linear_extrude(height = 36, twist = 5184.0) {
				polygon(points = [[9.4, 0], [10.6, 1.25], [9.4, 2.5]]);
			}
		}
	}
}
