import { Helmet } from 'react-helmet-async';
import { SEO_DEFAULTS } from '../i18n/siteStrings';

/** Default Open Graph / Twitter tags for link previews (pages can override via their own Helmet). */
export default function SocialMetaDefaults() {
  return (
    <Helmet>
      <meta property="og:type" content="website" />
      <meta property="og:site_name" content={SEO_DEFAULTS.siteName} />
      <meta property="og:url" content={SEO_DEFAULTS.siteUrl} />
      <meta property="og:image" content={SEO_DEFAULTS.ogImage} />
      <meta name="twitter:card" content={SEO_DEFAULTS.twitterCard} />
      <meta name="twitter:image" content={SEO_DEFAULTS.ogImage} />
    </Helmet>
  );
}
