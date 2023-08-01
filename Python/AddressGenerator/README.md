# Random Address Generator

This tool can be used to generate random company addresses. It is based on the [`random address`](https://github.com/neosergio/random-address) module.

## Usage

To generate a bunch of addresses, execute

```bash
./generate amount
```

And the generated addresses will be printed into a file `./data`.

## Example

```bash
~> ./generate 10
Begin data generation...
Data written to ./data seconds. 0 seconds remaining...

~> cat ./data
{"address1": "487 Maury Street", "address2": "", "city": "Montgomery", "state": "AL", "postalCode": "36104", "company": "Ink Boundless Navigate Merge Bloom S.C.S."}
{"address1": "3404 Lakeside Drive", "address2": "", "city": "Anchorage", "state": "AK", "postalCode": "99515", "company": "Green Net Mountain River Way BV"}
{"address1": "533 Forest Ridge Court", "address2": "", "city": "Montgomery", "state": "AL", "postalCode": "36109", "company": "Venture Ltda"}
{"address1": "1606 Trevilian Way", "address2": "", "city": "Louisville", "state": "KY", "postalCode": "40205", "company": "Data Dazzle Sun Explore Link Hub Pixel Ink Art Eco Co."}
{"address1": "303 Addison Drive", "address2": "", "city": "Glen Burnie", "state": "MD", "postalCode": "21060", "company": "Infinite Eternal Gleam Spark Infinite Seek Logic Link Bridge Oy"}
{"address1": "2829 31st Street Northwest", "address2": "", "city": "Washington", "state": "DC", "postalCode": "20008", "company": "Sun Apex Hub Heal Answer Power Earth Pinnacle Corp"}
{"address1": "6244 Sun River Drive", "address2": "", "city": "Sacramento", "state": "CA", "postalCode": "95824", "company": "Trek Patch Spark Nexus Earth Byte Seek Data Ltda"}
{"address1": "1636 Church Street Northwest", "address2": "", "city": "Washington", "state": "DC", "postalCode": "20036", "company": "Prime Seek Unending S.C.A."}
{"address1": "98 Lincoln Street", "address2": "", "city": "Revere", "state": "MA", "postalCode": "02151", "company": "Expedition Expedition Prime Sun Code Ocean Cloud Data Web Trek"}
{"address1": "1918 Spruce Street", "address2": "", "city": "Boulder", "state": "CO", "postalCode": "80302", "company": "Fix Axis Inc."}
```