difference() {
	cylinder($fn = 6, h = 120, r = 14.866769431632862);
	translate(v = [0, 0, 0]) {
		linear_extrude(center = false, height = 35, twist = 5040) {
			polygon(points = [[0, 0], [10.0, 0], [10.0, 0.5], [0, 1]]);
		}
	}
	translate(v = [0, 0, 85]) {
		linear_extrude(center = false, height = 35, twist = 5040) {
			polygon(points = [[0, 0], [10.0, 0], [10.0, 0.5], [0, 1]]);
		}
	}
}
