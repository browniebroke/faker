from typing import Dict, Optional, Tuple

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    # Format: (code, name)
    currencies: ElementsType[Tuple[str, str]] = (
        ("AED", "United Arab Emirates dirham"),
        ("AFN", "Afghan afghani"),
        ("ALL", "Albanian lek"),
        ("AMD", "Armenian dram"),
        ("ANG", "Netherlands Antillean guilder"),
        ("AOA", "Angolan kwanza"),
        ("ARS", "Argentine peso"),
        ("AUD", "Australian dollar"),
        ("AWG", "Aruban florin"),
        ("AZN", "Azerbaijani manat"),
        ("BAM", "Bosnia and Herzegovina convertible mark"),
        ("BBD", "Barbadian dollar"),
        ("BDT", "Bangladeshi taka"),
        ("BGN", "Bulgarian lev"),
        ("BHD", "Bahraini dinar"),
        ("BIF", "Burundian franc"),
        ("BMD", "Bermudian dollar"),
        ("BND", "Brunei dollar"),
        ("BOB", "Bolivian boliviano"),
        ("BRL", "Brazilian real"),
        ("BSD", "Bahamian dollar"),
        ("BTN", "Bhutanese ngultrum"),
        ("BWP", "Botswana pula"),
        ("BYR", "Belarusian ruble"),
        ("BZD", "Belize dollar"),
        ("CAD", "Canadian dollar"),
        ("CDF", "Congolese franc"),
        ("CHF", "Swiss franc"),
        ("CLP", "Chilean peso"),
        ("CNY", "Renminbi"),
        ("COP", "Colombian peso"),
        ("CRC", "Costa Rican colón"),
        ("CUC", "Cuban convertible peso"),
        ("CUP", "Cuban peso"),
        ("CVE", "Cape Verdean escudo"),
        ("CZK", "Czech koruna"),
        ("DJF", "Djiboutian franc"),
        ("DKK", "Danish krone"),
        ("DOP", "Dominican peso"),
        ("DZD", "Algerian dinar"),
        ("EGP", "Egyptian pound"),
        ("ERN", "Eritrean nakfa"),
        ("ETB", "Ethiopian birr"),
        ("EUR", "Euro"),
        ("FJD", "Fijian dollar"),
        ("FKP", "Falkland Islands pound"),
        ("GBP", "Pound sterling"),
        ("GEL", "Georgian lari"),
        ("GGP", "Guernsey pound"),
        ("GHS", "Ghanaian cedi"),
        ("GIP", "Gibraltar pound"),
        ("GMD", "Gambian dalasi"),
        ("GNF", "Guinean franc"),
        ("GTQ", "Guatemalan quetzal"),
        ("GYD", "Guyanese dollar"),
        ("HKD", "Hong Kong dollar"),
        ("HNL", "Honduran lempira"),
        ("HRK", "Croatian kuna"),
        ("HTG", "Haitian gourde"),
        ("HUF", "Hungarian forint"),
        ("IDR", "Indonesian rupiah"),
        ("ILS", "Israeli new shekel"),
        ("NIS", "Israeli new shekel"),
        ("IMP", "Manx pound"),
        ("INR", "Indian rupee"),
        ("IQD", "Iraqi dinar"),
        ("IRR", "Iranian rial"),
        ("ISK", "Icelandic króna"),
        ("JEP", "Jersey pound"),
        ("JMD", "Jamaican dollar"),
        ("JOD", "Jordanian dinar"),
        ("JPY", "Japanese yen"),
        ("KES", "Kenyan shilling"),
        ("KGS", "Kyrgyzstani som"),
        ("KHR", "Cambodian riel"),
        ("KMF", "Comorian franc"),
        ("KPW", "North Korean won"),
        ("KRW", "South Korean won"),
        ("KWD", "Kuwaiti dinar"),
        ("KYD", "Cayman Islands dollar"),
        ("KZT", "Kazakhstani tenge"),
        ("LAK", "Lao kip"),
        ("LBP", "Lebanese pound"),
        ("LKR", "Sri Lankan rupee"),
        ("LRD", "Liberian dollar"),
        ("LSL", "Lesotho loti"),
        ("LTL", "Lithuanian litas"),
        ("LYD", "Libyan dinar"),
        ("MAD", "Moroccan dirham"),
        ("MDL", "Moldovan leu"),
        ("MGA", "Malagasy ariar"),
        ("MKD", "Macedonian denar"),
        ("MMK", "Burmese kyat"),
        ("MNT", "Mongolian tugrik"),
        ("MOP", "Macanese pataca"),
        ("MRO", "Mauritanian ouguiya"),
        ("MUR", "Mauritian rupee"),
        ("MVR", "Maldivian rufiyaa"),
        ("MWK", "Malawian kwacha"),
        ("MXN", "Mexican peso"),
        ("MYR", "Malaysian ringgit"),
        ("MZN", "Mozambican metical"),
        ("NAD", "Namibian dollar"),
        ("NGN", "Nigerian naira"),
        ("NIO", "Nicaraguan córdoba"),
        ("NOK", "Norwegian krone"),
        ("NPR", "Nepalese rupee"),
        ("NZD", "New Zealand dollar"),
        ("OMR", "Omani rial"),
        ("PAB", "Panamanian balboa"),
        ("PEN", "Peruvian sol"),
        ("PGK", "Papua New Guinean kina"),
        ("PHP", "Philippine peso"),
        ("PKR", "Pakistani rupee"),
        ("PLN", "Polish zloty"),
        ("PYG", "Paraguayan guarani"),
        ("QAR", "Qatari riyal"),
        ("RON", "Romanian leu"),
        ("RSD", "Serbian dinar"),
        ("RUB", "Russian ruble"),
        ("RWF", "Rwandan franc"),
        ("SAR", "Saudi riyal"),
        ("SBD", "Solomon Islands dollar"),
        ("SCR", "Seychellois rupee"),
        ("SDG", "Sudanese pound"),
        ("SEK", "Swedish krona"),
        ("SGD", "Singapore dollar"),
        ("SHP", "Saint Helena pound"),
        ("SLL", "Sierra Leonean leone"),
        ("SOS", "Somali shilling"),
        ("SPL", "Seborga luigino"),
        ("SRD", "Surinamese dollar"),
        ("STD", "São Tomé and Príncipe dobra"),
        ("SVC", "Salvadoran colón"),
        ("SYP", "Syrian pound"),
        ("SZL", "Swazi lilangeni"),
        ("THB", "Thai baht"),
        ("TJS", "Tajikistani somoni"),
        ("TMT", "Turkmenistan manat"),
        ("TND", "Tunisian dinar"),
        ("TOP", "Tongan paʻanga"),
        ("TRY", "Turkish lira"),
        ("TTD", "Trinidad and Tobago dollar"),
        ("TVD", "Tuvaluan dollar"),
        ("TWD", "New Taiwan dollar"),
        ("TZS", "Tanzanian shilling"),
        ("UAH", "Ukrainian hryvnia"),
        ("UGX", "Ugandan shilling"),
        ("USD", "United States dollar"),
        ("UYU", "Uruguayan peso"),
        ("UZS", "Uzbekistani soʻm"),
        ("VEF", "Venezuelan bolívar"),
        ("VND", "Vietnamese đồng"),
        ("VUV", "Vanuatu vatu"),
        ("WST", "Samoan tālā"),
        ("XAF", "Central African CFA franc"),
        ("XCD", "Eastern Caribbean dollar"),
        ("XDR", "Special drawing rights"),
        ("XOF", "West African CFA franc"),
        ("XPF", "CFP franc"),
        ("YER", "Yemeni rial"),
        ("ZAR", "South African rand"),
        ("ZMW", "Zambian kwacha"),
        ("ZWD", "Zimbabwean dollar"),
    )

    # Source: https://en.wikipedia.org/wiki/List_of_cryptocurrencies
    cryptocurrencies: ElementsType[Tuple[str, str]] = (
        ("AMP", "AMP"),
        ("AUR", "Auroracoin"),
        ("BC", "BlackCoin"),
        ("BTC", "Bitcoin"),
        ("BURST", "Burstcoin"),
        ("DASH", "Dash"),
        ("DOGE", "Dogecoin"),
        ("EMC", "Emercoin"),
        ("ETH", "Ethereum"),
        ("ETC", "Ethereum Classic"),
        ("GRC", "Gridcoin"),
        ("KOI", "Coinye"),
        ("LTC", "Litecoin"),
        ("MSC", "Omni"),
        ("MZC", "MazaCoin"),
        ("NMC", "Namecoin"),
        ("NXT", "Nxt"),
        ("POT", "PotCoin"),
        ("PPC", "Peercoin"),
        ("TIT", "Titcoin"),
        ("VTC", "Vertcoin"),
        ("XDN", "DigitalNote"),
        ("XMR", "Monero"),
        ("XPM", "Primecoin"),
        ("XRP", "Ripple"),
        ("ZEC", "Zcash"),
        ("STC", "SwiftCoin"),
        ("BCN", "Bytecoin"),
        ("FTH", "Feathercoin"),
        ("NEO", "NEO"),
        ("NEM", "XEM"),
        ("USDT", "Tether"),
        ("IOTA", "IOTA"),
        ("DRC", "Decred"),
        ("WAVES", "Waves Platform"),
        ("LSK", "Lisk"),
        ("ZCL", "Zclassic"),
        ("BCH", "Bitcoin Cash"),
        ("UBQ", "Ubiq"),
        ("EOS", "EOS.IO"),
        ("SRN", "Sirin Labs"),
        ("TRX", "TRON"),
        ("ADA", "Cardano"),
    )

    # List of currency symbols in Unicode, source: https://www.unicode.org/charts/beta/nameslist/n_20A0.html
    currency_symbols: Dict[str, str] = {
        "AFN": "\u060B",
        "ANG": "\u0192",
        "ARS": "\u0024",
        "AUD": "\u0024",
        "AWG": "\u0192",
        "BBD": "\u0024",
        "BDT": "\u09F3",
        "BMD": "\u0024",
        "BND": "\u0024",
        "BOB": "\u0024",
        "BRL": "\u0024",
        "BSD": "\u0024",
        "BZD": "\u0024",
        "CAD": "\u0024",
        "CLP": "\u0024",
        "CNY": "\u00A5",
        "COP": "\u0024",
        "CRC": "\u20A1",
        "CUP": "\u0024",
        "CVE": "\u0024",
        "DOP": "\u0024",
        "EGP": "\u00A3",
        "EUR": "\u20AC",
        "FJD": "\u0024",
        "FKP": "\u00A3",
        "GBP": "\u00A3",
        "GHS": "\u20B5",
        "GIP": "\u00A3",
        "GYD": "\u0024",
        "HKD": "\u0024",
        "HUF": "\u0192",
        "IDR": "\u20A8",
        "ILS": "\u20AA",
        "INR": "\u20B9",
        "IRR": "\uFDFC",
        "JMD": "\u0024",
        "JPY": "\u00A5",
        "KHR": "\u17DB",
        "KPW": "\u20A9",
        "KRW": "\u20A9",
        "KYD": "\u0024",
        "KZT": "\u20B8",
        "LAK": "\u20AD",
        "LBP": "\u00A3",
        "LKR": "\u20A8",
        "LRD": "\u0024",
        "MNT": "\u20AE",
        "MOP": "\u0024",
        "MUR": "\u20A8",
        "MXN": "\u0024",
        "NAD": "\u0024",
        "NGN": "\u20A6",
        "NIO": "\u0024",
        "NPR": "\u20A8",
        "NZD": "\u0024",
        "OMR": "\uFDFC",
        "PHP": "\u20B1",
        "PKR": "\u20A8",
        "PYG": "\u20B2",
        "QAR": "\uFDFC",
        "RUB": "\u20BD",
        "SAR": "\uFDFC",
        "SBD": "\u0024",
        "SDG": "\u00A3",
        "SGD": "\u0024",
        "SHP": "\u00A3",
        "SRD": "\u0024",
        "SYP": "\u00A3",
        "THB": "\u0E3F",
        "TOP": "\u0024",
        "TRY": "\u20BA",
        "TTD": "\u0024",
        "TWD": "\u0024",
        "UAH": "\u20B4",
        "USD": "\u0024",
        "UY": "\u0024",
        "VND": "\u20AB",
        "WST": "\u0024",
        "XCD": "\u0024",
        "YER": "\uFDFC",
        "ZWD": "\u0024",
    }

    price_formats: ElementsType[str] = ["#.##", "%#.##", "%##.##", "%,###.##", "%#,###.##"]

    def currency(self) -> Tuple[str, str]:
        return self.random_element(self.currencies)

    def currency_code(self) -> str:
        return self.currency()[0]

    def currency_name(self) -> str:
        return self.currency()[1]

    def currency_symbol(self, code: Optional[str] = None) -> str:
        """
        :example: $
        """
        if code is None:
            code = self.random_element(self.currency_symbols.keys())
        return self.currency_symbols[code]

    def cryptocurrency(self) -> Tuple[str, str]:
        return self.random_element(self.cryptocurrencies)

    def cryptocurrency_code(self) -> str:
        return self.cryptocurrency()[0]

    def cryptocurrency_name(self) -> str:
        return self.cryptocurrency()[1]

    def pricetag(self) -> str:
        currency: Tuple[str, str] = self.random_element(self.currencies)
        return currency[0] + "\N{no-break space}" + self.numerify(self.random_element(self.price_formats))
