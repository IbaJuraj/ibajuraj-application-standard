import XCTest

enum IJStandardUIID {
    static let settingsAboutRow = "ij.settings.about.row"
    static let aboutVersionCard = "ij.about.version.card"
    static let aboutStandardCard = "ij.about.standard.card"
    static let aboutDeveloperCard = "ij.about.developer.card"
    static let aboutWebRow = "ij.about.web.row"
    static let aboutPrivacyRow = "ij.about.privacy.row"
    static let appearanceModeControl = "ij.appearance.mode.control"
    static let appearanceThemeList = "ij.appearance.theme.list"
    static let bottomNavigation = "ij.bottomnav.container"
    static let bottomPrimaryAction = "ij.bottomnav.primaryAction"
}

extension XCUIApplication {
    func assertCommonAboutSurface(file: StaticString = #filePath, line: UInt = #line) {
        XCTAssertTrue(descendants(matching: .any)[IJStandardUIID.aboutVersionCard].exists, file: file, line: line)
        XCTAssertTrue(descendants(matching: .any)[IJStandardUIID.aboutStandardCard].exists, file: file, line: line)
        XCTAssertTrue(descendants(matching: .any)[IJStandardUIID.aboutDeveloperCard].exists, file: file, line: line)
    }
}
