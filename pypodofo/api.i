%module api
%{
#include <base/PdfDefines.h>
#include <base/PdfString.h>
#include <base/PdfError.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>

using namespace PoDoFo;
%}

#include <base/PdfDefines.h>
#include <base/PdfString.h>
#include <base/PdfError.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>


typedef ptrdiff_t pdf_long;

enum EPdfField {
    ePdfField_PushButton,
    ePdfField_CheckBox,
    ePdfField_RadioButton,
    ePdfField_TextField,
    ePdfField_ComboBox,
    ePdfField_ListBox,
    ePdfField_Signature,

    ePdfField_Unknown = 0xff
};


enum EPdfError {
    ePdfError_ErrOk = 0,                /**< The default value indicating no error. */

    ePdfError_TestFailed,               /**< Used in PoDoFo tests, to indicate that a test failed for some reason. */

    ePdfError_InvalidHandle,            /**< Null pointer was passed, but null pointer is not allowed. */
    ePdfError_FileNotFound,             /**< A file was not found or cannot be opened. */
    ePdfError_InvalidDeviceOperation,	/**< Tried to do something unsupported to an I/O device like seek a non-seekable input device */
    ePdfError_UnexpectedEOF,            /**< End of file was reached but data was expected. */
    ePdfError_OutOfMemory,              /**< Not enough memory to complete an operation. */
    ePdfError_ValueOutOfRange,          /**< The specified memory is out of the allowed range. */
    ePdfError_InternalLogic,            /**< An internal sanity check or assertion failed. */ 
    ePdfError_InvalidEnumValue,         /**< An invalid enum value was specified. */

    ePdfError_PageNotFound,             /**< The requested page could not be found in the PDF. */

    ePdfError_NoPdfFile,                /**< The file is no PDF file. */
    ePdfError_NoXRef,                   /**< The PDF file has no or an invalid XRef table. */
    ePdfError_NoTrailer,                /**< The PDF file has no or an invalid trailer. */
    ePdfError_NoNumber,                 /**< A number was expected in the PDF file, but the read string is no number. */
    ePdfError_NoObject,                 /**< A object was expected and non was found. */
    ePdfError_NoEOFToken,               /**< The PDF file has no or an invalid EOF marker. */

    ePdfError_InvalidTrailerSize,       /**< The trailer size is invalid. */
    ePdfError_InvalidLinearization,     /**< The linearization directory of a web-optimized PDF file is invalid. */
    ePdfError_InvalidDataType,          /**< The passed datatype is invalid or was not recognized */
    ePdfError_InvalidXRef,              /**< The XRef table is invalid */
    ePdfError_InvalidXRefStream,        /**< A XRef steam is invalid */
    ePdfError_InvalidXRefType,          /**< The XRef type is invalid or was not found */
    ePdfError_InvalidPredictor,         /**< Invalid or unimplemented predictor */
    ePdfError_InvalidStrokeStyle,       /**< Invalid stroke style during drawing */
    ePdfError_InvalidHexString,         /**< Invalid hex string */
    ePdfError_InvalidStream,            /**< The stream is invalid */
    ePdfError_InvalidStreamLength,      /**< The stream length is invlaid */
    ePdfError_InvalidKey,               /**< The specified key is invalid */
    ePdfError_InvalidName,              /**< The specified Name is not valid in this context */
    ePdfError_InvalidEncryptionDict,    /**< The encryption dictionary is invalid or misses a required key */
    ePdfError_InvalidPassword,          /**< The password used to open the PDF file was invalid */
    ePdfError_InvalidFontFile,          /**< The font file is invalid */
    ePdfError_InvalidContentStream,     /**< The content stream is invalid due to mismatched context pairing or other problems */

    ePdfError_UnsupportedFilter,        /**< The requested filter is not yet implemented. */
    ePdfError_UnsupportedFontFormat,    /**< This font format is not supported by PoDoFO. */
    ePdfError_ActionAlreadyPresent,     /**< An Action was already present when trying to add a Destination */
    ePdfError_WrongDestinationType,     /**< The requested field is not available for the given destination type */

    ePdfError_MissingEndStream,         /**< The required token endstream was not found. */
    ePdfError_Date,                     /**< Date/time error */
    ePdfError_Flate,                    /**< Error in zlib */
    ePdfError_FreeType,                 /**< Error in FreeType */
    ePdfError_SignatureError,           /**< Error in signature */

    ePdfError_MutexError,               /**< Error during a mutex operation */

    ePdfError_UnsupportedImageFormat,   /**< This image format is not supported by PoDoFO. */
    ePdfError_CannotConvertColor,       /**< This color format cannot be converted. */

    ePdfError_NotImplemented,           /**< This feature is currently not implemented. */

    ePdfError_DestinationAlreadyPresent,/**< An destination was already present when trying to add a Action */
    ePdfError_ChangeOnImmutable,        /**< Changing values on immutable objects is not allowed. */

    ePdfError_NotCompiled,              /**< This feature was disabled during compile time. */

    ePdfError_Unknown = 0xffff          /**< Unknown error */
};


class PdfError {
public:
    const char *what() const;
    EPdfError GetError() const;
    const char *ErrorMessage(EPdfError eCode);
    virtual ~PdfError() throw();
};


class PdfMemDocument {
public:
    PdfMemDocument(const char*) throw (PdfError);
    ~PdfMemDocument();

    int GetPageCount() const;
    PdfPage *GetPage(int) const;
    void Write(const char *);
};


class PdfPage {
public:
    PdfPage( PdfObject* pObject, const std::deque<PdfObject*> & listOfParents );
    int GetNumFields() const;
    const PdfField GetField(int) const;
    unsigned int GetPageNumber() const;
};

// Map PdfString as python string
%typemap(out) PdfString {
    $result = PyString_FromString($1.GetString());
}

// Map python string as PdfString
%typemap(typecheck, precedence=SWIG_TYPECHECK_POINTER) const PdfString & {
    $1 = PyString_Check($input) ? 1 : 0;
}

%typemap(in) const PdfString & (PdfString temp) {
    temp = PdfString(PyString_AsString($input));
    $1 = &temp;
}

class PdfField {
public:
    PdfField(const PdfField &) throw(PdfError);
    PdfString GetFieldName() const;
    PdfPage *GetPage() const;
    void SetFieldName(const PdfString&);
    EPdfField GetType() const;
};


class PdfTextField : public PdfField {
public:
    PdfTextField(const PdfField &) throw(PdfError);
    void SetText(const PdfString &) throw (PdfError);
    PdfString GetText() const;
    void SetMaxLen( pdf_long nMaxLen );
    pdf_long GetMaxLen() const;
};


class PdfListField : public PdfField {
public:
    PdfListField(const PdfField &) throw(PdfError);
    void InsertItem(const PdfString &rsValue, const PdfString &rsDisplayName=PdfString::StringNull);
    const PdfString GetItem(int) const;
    void RemoveItem(int);
    size_t GetItemCount() const;
    void SetSelectedItem(int);
    int GetSelectedItem() const;
};


class PdfComboBox : public PdfListField {
public:
    PdfComboBox(const PdfField &) throw(PdfError);
    void SetEditable(bool bEdit);
    bool IsEditable() const;
};


class PdfButton : public PdfField {
public:
    PdfButton(const PdfField &) throw(PdfError);
    bool IsPushButton() const;
    bool IsCheckBox() const;
    bool IsRadioButton() const;
    void SetCaption(const PdfString &rsText);
    const PdfString GetCaption() const;
};

class PdfPushButton : public PdfButton {
public:
    PdfPushButton(const PdfField &) throw(PdfError);
};


class PdfCheckBox : public PdfButton {
public:
    PdfCheckBox(const PdfField &) throw(PdfError);
    void SetChecked(bool bChecked);
    bool IsChecked() const;

};


class PdfString {
public:
    PdfString(const char *, const PdfEncoding * const pEncoding=NULL);
    const char* GetString() const;
};
