# Naming things
## Variables, Functions, Classes, Constants

[Presentation on Naming](https://www.slideshare.net/CleanestCode/naming-standards-clean-code)

[Clean Code Summary](https://www.slideshare.net/Edorian/stop-wastingtimebyapplyingcleancodeprinciples/22-Organizational_structures)

## Where do short variable names come from?
* [Old maths and physics writing by hand](https://softwareengineering.stackexchange.com/questions/176582/is-there-an-excuse-for-short-variable-names#176585)
* C code base
* Small code bases
* Assembly code bases


## How we should name things
* meaningful names
* if the name requires a comment, change the name.
* avoid disinformation
* comments can be good and bad
* the purpose of a name is to reveal its intent
  * why it exists
  * how its used
  * what it does

## Examples
* Bad:
  * getId, getName, getBMI, setWeight
* Good:
  * getUserId, getFirst/Last/DisplayName, getBodyMassIndex

* Bad
<code>
class Calendar {
  public function getMonth($short = false){...}
}
</code>
* Good
<code>
class Calendar {
  public function get*MonthNames*(){...}
  public function get*ShortMonth*Names(){...}
}
</code>

* Proper naming is important and easy to neglect
  * Descriptive names communicate intent
  * They enable us to understand whats up
  * They reduce the mental mapping effort
  * Misleading names can make reading code almost impossible
* Writing names for a machine to understand is easy, but writing for humans is hard.

* When in doubt use a style guide or agree to one.
  * Go - [Effective Go](https://golang.org/doc/effective_go.htm)
  * PHP - [PHP Standar Recommendations - PSR's](https://www.php-fig.org/psr/)
  * JS - [AirBnB Style Guide](https://github.com/airbnb/javascript)

## Temporary Variables
### Iterators
### For loop
