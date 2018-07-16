/**
 * Created by Abderrahim on 16/02/2017.
 */
if (!String.prototype.contains) {
    String.prototype.contains = function(s) {
        return this.indexOf(s) > -1
    }
}