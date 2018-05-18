"use strict"
class Can {

    constructor(radius, height) {
	this.radius = radius
	this.height = height
    }

    get volume() {
	return this.radius * this.radius * Math.PI * this.height
    }
}
